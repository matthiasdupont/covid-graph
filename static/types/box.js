import {Element} from 'chart.js';
import {scaleValue, roundedRect} from '../helpers';

export default class BoxAnnotation extends Element {
	inRange(mouseX, mouseY, useFinalPosition) {
		const {x, y, width, height} = this.getProps(['x', 'y', 'width', 'height'], useFinalPosition);

		return mouseX >= x &&
			mouseX <= x + width &&
			mouseY >= y &&
			mouseY <= y + height;
	}

	getCenterPoint(useFinalPosition) {
		const {x, y, width, height} = this.getProps(['x', 'y', 'width', 'height'], useFinalPosition);
		return {
			x: x + width / 2,
			y: y + height / 2
		};
	}

	draw(ctx) {
		const {x, y, width, height, options} = this;

		ctx.save();

		ctx.lineWidth = options.borderWidth;
		ctx.strokeStyle = options.borderColor;
		ctx.fillStyle = options.backgroundColor;

		ctx.beginPath();
		roundedRect(ctx, x, y, width, height);
		ctx.fill();
		ctx.stroke();

		ctx.restore();
	}

	resolveElementProperties(chart, options) {
		const xScale = chart.scales[options.xScaleID];
		const yScale = chart.scales[options.yScaleID];
		let {top: y, left: x, bottom: y2, right: x2} = chart.chartArea;
		let min, max;

		if (!xScale && !yScale) {
			return {options: {}};
		}

		if (xScale) {
			min = scaleValue(xScale, options.xMin, x);
			max = scaleValue(xScale, options.xMax, x2);
			x = Math.min(min, max);
			x2 = Math.max(min, max);
		}

		if (yScale) {
			min = scaleValue(yScale, options.yMin, y2);
			max = scaleValue(yScale, options.yMax, y);
			y = Math.min(min, max);
			y2 = Math.max(min, max);
		}

		return {
			x,
			y,
			x2,
			y2,
			width: x2 - x,
			height: y2 - y
		};
	}
}

BoxAnnotation.id = 'boxAnnotation';

BoxAnnotation.defaults = {
	display: true,
	borderWidth: 1
};

BoxAnnotation.defaultRoutes = {
	borderColor: 'color',
	backgroundColor: 'color'
};
