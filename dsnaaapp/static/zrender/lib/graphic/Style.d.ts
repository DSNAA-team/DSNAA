import { RectLike } from '../core/BoundingRect';
import Displayable from './Displayable';
import { VectorArray } from '../core/vector';
import { Dictionary, PropType, TextVerticalAlign, ImageLike, TextAlign } from '../core/types';
import { LinearGradientObject } from './LinearGradient';
import { RadialGradientObject } from './RadialGradient';
import { PatternObject } from './Pattern';
import { GradientObject } from './Gradient';
export declare class TextStyleOption {
    text?: string;
    textFill?: string | PatternObject | LinearGradientObject | RadialGradientObject;
    textStroke?: string | PatternObject | LinearGradientObject | RadialGradientObject;
    textStrokeWidth?: number;
    font?: string;
    textFont?: string;
    fontStyle?: string;
    fontWeight?: string;
    fontFamily?: string;
    fontSize?: number;
    textAlign?: TextAlign;
    textVerticalAlign?: TextVerticalAlign;
    textBaseline?: TextVerticalAlign;
    textLineHeight?: number;
    textWidth?: number | string;
    textHeight?: number;
    textTag?: string;
    textShadowColor?: string;
    textShadowBlur?: number;
    textShadowOffsetX?: number;
    textShadowOffsetY?: number;
    textBackgroundColor?: string | {
        image: ImageLike | string;
    };
    textPadding?: number | number[];
    textBorderColor?: string;
    textBorderWidth?: number;
    textBorderRadius?: number | number[];
    textBoxShadowColor?: string;
    textBoxShadowBlur?: number;
    textBoxShadowOffsetX?: number;
    textBoxShadowOffsetY?: number;
}
export declare class StyleOption extends TextStyleOption {
    x?: number;
    y?: number;
    fill?: string | PatternObject | LinearGradientObject | RadialGradientObject;
    stroke?: string | PatternObject | LinearGradientObject | RadialGradientObject;
    opacity?: number;
    fillOpacity?: number;
    strokeOpacity?: number;
    lineDash?: false | number[];
    lineDashOffset?: number;
    shadowBlur?: number;
    shadowOffsetX?: number;
    shadowOffsetY?: number;
    shadowColor?: string;
    lineWidth?: number;
    lineCap?: CanvasLineCap;
    lineJoin?: CanvasLineJoin;
    miterLimit?: number;
    strokeNoScale?: boolean;
    text?: string;
    textPosition?: string | number[];
    textRect?: RectLike;
    textOffset?: number[];
    textDistance?: number;
    transformText?: boolean;
    textRotation?: number;
    textOrigin?: 'center' | VectorArray;
    textPadding?: number | number[];
    rich?: Dictionary<TextStyleOption>;
    truncate?: {
        outerWidth?: number;
        outerHeight?: number;
        ellipsis?: string;
        placeholder?: string;
        minChar?: number;
    };
    blend?: string;
}
declare type StyleKey = keyof StyleOption;
declare type StyleValueType = PropType<StyleOption, StyleKey>;
export default class Style extends StyleOption {
    constructor(opts?: StyleOption);
    bind(ctx: CanvasRenderingContext2D, el: Displayable, prevEl: Displayable): void;
    hasFill(): boolean;
    hasStroke(): boolean;
    extendFrom(otherStyle: StyleOption, overwrite?: boolean): void;
    set(obj: StyleOption | StyleKey, value?: StyleValueType): void;
    clone(): Style;
    static getGradient(ctx: CanvasRenderingContext2D, obj: GradientObject, rect: RectLike): CanvasGradient;
    private static initDefaultProps;
}
export {};
