import React from 'react';
import { queryAllByAltText, render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import {Product} from "../../types";

const testProduct: Product = {
    id: 1,
    name: 'test 1',
    description: 'test 1',
    price: 1,
    priceSymbol: '$',
    category: 'Электроника',
    imgUrl: '1.png',
};

const testProductNoImg: Product = {
    id: 2,
    name: 'test 2',
    description: 'test 2',
    price: 2,
    priceSymbol: '$',
    category: 'Электроника',
};

describe('ProductCard test', () => {

    it('should render correctly', () => {
        const rendered = render(<ProductCard {...testProduct} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should display product correctly with image', () => {
        const rendered = render(<ProductCard {...testProduct} />);
        expect(rendered.queryByAltText('test 1')).toBeInTheDocument();
    });

    it('should display product correctly without image', () => {
        const rendered = render(<ProductCard {...testProductNoImg} />);
        expect(rendered.queryByAltText('test 2')).not.toBeInTheDocument();
    });
});
