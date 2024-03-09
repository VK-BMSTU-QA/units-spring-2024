import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import {Product} from "../../types";

const product: Product = {
    id: 1,
    name: '1',
    description: '1',
    price: 1,
    priceSymbol: '$',
    category: 'Электроника',
    imgUrl: '1.png',
};

const productNoImg: Product = {
    id: 1,
    name: '1',
    description: '1',
    price: 1,
    priceSymbol: '$',
    category: 'Электроника',
};

describe('test ProductCard test', () => {

    it('should render correctly ', () => {
        const rendered = render(<ProductCard {...product} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render correctly without image', () => {
        const rendered = render(<ProductCard {...productNoImg} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });
});