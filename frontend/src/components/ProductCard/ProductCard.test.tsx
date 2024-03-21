import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import {Product} from "../../types";

describe('ProductCard test', () => {
    const product: Product = {
        id: 1,
        name: 'IPhone 14 Pro',
        description: 'Latest iphone, buy it now',
        price: 999,
        priceSymbol: '$',
        category: 'Электроника',
        imgUrl: '/iphone.png',
    };

    it('should render correctly with image', () => {
        const { asFragment } = render(<ProductCard {...product} />);
        expect(asFragment()).toMatchSnapshot();
    });

    it('should render correctly without image', () => {
        const productWithoutImg = { ...product, imgUrl: undefined };
        const { asFragment } = render(<ProductCard {...productWithoutImg} />);
        expect(asFragment()).toMatchSnapshot();
    });
});
