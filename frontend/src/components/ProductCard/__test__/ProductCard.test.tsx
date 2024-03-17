import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard }  from '../ProductCard';

import { Product } from '../../../types';

const sampleProduct: Product = {
    id: 1,
    name: 'IPhone 14 Pro',
    description: 'Latest iphone, buy it now',
    price: 999,
    priceSymbol: '$',
    category: 'Электроника',
    imgUrl: 'image.png'
}

describe('ProductCard test', () => {
    it('should render correctly', () => {
        const rendered = render(<ProductCard {...sampleProduct} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should display product details', () => {
        const rendered = render(<ProductCard {...sampleProduct} />);

        expect(rendered.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(rendered.getByText('Latest iphone, buy it now')).toBeInTheDocument();
        expect(rendered.getByText('999 $')).toBeInTheDocument();
        expect(rendered.getByText('Электроника')).toBeInTheDocument();
    });

    it('should render an image when imgUrl is provided', () => {
        const rendered = render(<ProductCard {...sampleProduct} />);

        expect(rendered.getByAltText('IPhone 14 Pro')).toBeInTheDocument();
    });

    it('should not render an image when imgUrl is not provided', () => {
        const productWithoutImage = { ...sampleProduct, imgUrl: undefined };
        const rendered = render(<ProductCard {...productWithoutImage} />);

        expect(rendered.queryByAltText('IPhone 14 Pro')).toBeNull();
    });
});
