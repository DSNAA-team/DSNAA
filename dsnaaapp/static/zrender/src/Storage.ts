import * as util from './core/util';
import env from './core/env';
import Group from './graphic/Group';
import Element from './Element';

// Use timsort because in most case elements are partially sorted
// https://jsfiddle.net/pissang/jr4x7mdm/8/
import timsort from './core/timsort';
import Displayable from './graphic/Displayable';
import Path from './graphic/Path';
import { REDARAW_BIT } from './graphic/constants';

let invalidZErrorLogged = false;
function logInvalidZError() {
    if (invalidZErrorLogged) {
        return;
    }
    invalidZErrorLogged = true;
    console.warn('z / z2 / zlevel of displayable is invalid, which may cause unexpected errors');
}

function shapeCompareFunc(a: Displayable, b: Displayable) {
    if (a.zlevel === b.zlevel) {
        if (a.z === b.z) {
            // if (a.z2 === b.z2) {
            //     // FIXME Slow has renderidx compare
            //     // http://stackoverflow.com/questions/20883421/sorting-in-javascript-should-every-compare-function-have-a-return-0-statement
            //     // https://github.com/v8/v8/blob/47cce544a31ed5577ffe2963f67acb4144ee0232/src/js/array.js#L1012
            //     return a.__renderidx - b.__renderidx;
            // }
            return a.z2 - b.z2;
        }
        return a.z - b.z;
    }
    return a.zlevel - b.zlevel;
}

export default class Storage {

    private _roots: Element[] = []

    private _displayList: Displayable[] = []

    private _displayListLen = 0

    traverse<T>(
        cb: (this: T, el: Element) => void,
        context?: T
    ) {
        for (let i = 0; i < this._roots.length; i++) {
            this._roots[i].traverse(cb, context);
        }
    }

    /**
     * get a list of elements to be rendered
     *
     * @param {boolean} update whether to update elements before return
     * @param {DisplayParams} params options
     * @return {Displayable[]} a list of elements
     */
    getDisplayList(update?: boolean, includeIgnore?: boolean): Displayable[] {
        includeIgnore = includeIgnore || false;
        const displayList = this._displayList;
        // If displaylist is not created yet. Update force
        if (update || !displayList.length) {
            this.updateDisplayList(includeIgnore);
        }
        return displayList;
    }

    /**
     * ??????????????????????????????
     * ???????????????????????????????????????????????????????????????????????????????????????Group???Shape?????????????????????????????????Shape?????????????????????
     * ?????????????????????????????????zlevel > z > ???????????????????????????????????????
     */
    updateDisplayList(includeIgnore?: boolean) {
        this._displayListLen = 0;

        const roots = this._roots;
        const displayList = this._displayList;
        for (let i = 0, len = roots.length; i < len; i++) {
            this._updateAndAddDisplayable(roots[i], null, includeIgnore);
        }

        displayList.length = this._displayListLen;

        env.canvasSupported && timsort(displayList, shapeCompareFunc);
    }

    private _updateAndAddDisplayable(
        el: Element,
        clipPaths: Path[],
        includeIgnore?: boolean
    ) {
        if (el.ignore && !includeIgnore) {
            return;
        }

        el.beforeUpdate();
        el.update();
        el.afterUpdate();

        const userSetClipPath = el.getClipPath();

        if (el.ignoreClip) {
            clipPaths = null;
        }
        else if (userSetClipPath) {

            // FIXME ????????????
            if (clipPaths) {
                clipPaths = clipPaths.slice();
            }
            else {
                clipPaths = [];
            }

            let currentClipPath = userSetClipPath;
            let parentClipPath = el;
            // Recursively add clip path
            while (currentClipPath) {
                // clipPath ?????????????????????????????? clipPath ?????????
                // TODO: parent should be group type.
                currentClipPath.parent = parentClipPath as Group;
                currentClipPath.updateTransform();

                clipPaths.push(currentClipPath);

                parentClipPath = currentClipPath;
                currentClipPath = currentClipPath.getClipPath();
            }
        }

        // ZRText and Group and combining morphing Path may use children
        if ((el as Group).childrenRef) {
            const children = (el as Group).childrenRef();

            for (let i = 0; i < children.length; i++) {
                const child = children[i];

                // Force to mark as dirty if group is dirty
                if (el.__dirty) {
                    child.__dirty |= REDARAW_BIT;
                }

                this._updateAndAddDisplayable(child, clipPaths, includeIgnore);
            }

            // Mark group clean here
            el.__dirty = 0;

        }
        else {
            const disp = el as Displayable;
            // Element is displayable
            if (clipPaths && clipPaths.length) {
                disp.__clipPaths = clipPaths;
            }
            else if (disp.__clipPaths && disp.__clipPaths.length > 0) {
                disp.__clipPaths = [];
            }

            // Avoid invalid z, z2, zlevel cause sorting error.
            if (isNaN(disp.z)) {
                logInvalidZError();
                disp.z = 0;
            }
            if (isNaN(disp.z2)) {
                logInvalidZError();
                disp.z2 = 0;
            }
            if (isNaN(disp.zlevel)) {
                logInvalidZError();
                disp.zlevel = 0;
            }

            this._displayList[this._displayListLen++] = disp;
        }

        // Add decal
        const decalEl = (el as Path).getDecalElement && (el as Path).getDecalElement();
        if (decalEl) {
            this._updateAndAddDisplayable(decalEl, clipPaths, includeIgnore);
        }

        // Add attached text element and guide line.
        const textGuide = el.getTextGuideLine();
        if (textGuide) {
            this._updateAndAddDisplayable(textGuide, clipPaths, includeIgnore);
        }

        const textEl = el.getTextContent();
        if (textEl) {
            this._updateAndAddDisplayable(textEl, clipPaths, includeIgnore);
        }
    }

    /**
     * ????????????(Displayable)?????????(Group)????????????
     */
    addRoot(el: Element) {
        if (el.__zr && el.__zr.storage === this) {
            return;
        }

        this._roots.push(el);
    }

    /**
     * ?????????????????????(Displayable)?????????(Group)
     * @param el
     */
    delRoot(el: Element | Element[]) {

        if (el instanceof Array) {
            for (let i = 0, l = el.length; i < l; i++) {
                this.delRoot(el[i]);
            }
            return;
        }

        const idx = util.indexOf(this._roots, el);
        if (idx >= 0) {
            this._roots.splice(idx, 1);
        }
    }

    delAllRoots() {
        this._roots = [];
        this._displayList = [];
        this._displayListLen = 0;

        return;
    }

    getRoots() {
        return this._roots;
    }

    /**
     * ??????????????????Storage
     */
    dispose() {
        this._displayList = null;
        this._roots = null;
    }

    displayableSortFunc = shapeCompareFunc
}