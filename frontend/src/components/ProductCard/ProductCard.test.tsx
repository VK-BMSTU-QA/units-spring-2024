import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import {Product} from "../../types";

const testProduct: Product = {
    id: 1,
    name: '1',
    description: '1',
    price: 1,
    priceSymbol: '$',
    category: 'Электроника',
    imgUrl: '1.png',
};

const testProductNoImg: Product = {
    id: 2,
    name: '2',
    description: '2',
    price: 2,
    priceSymbol: '$',
    category: 'Электроника',
};

describe('ProductCard test', () => {

    it('should render correctly with image', () => {
        const rendered = render(<ProductCard {...testProduct} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render correctly without image', () => {
        const rendered = render(<ProductCard {...testProductNoImg} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });
});