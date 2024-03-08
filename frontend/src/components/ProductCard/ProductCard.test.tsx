import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import { ProductCard } from './ProductCard';
import { Product } from '../../types';

describe('ProductCard component tests', () => {
    const product: Product = {
        id: 0,
        name: 'Test Product',
        description: 'This is a test product',
        price: 100,
        priceSymbol: '$',
        category: 'Электроника',
        imgUrl: 'test.jpg',
    };

    it('should render correctly', () => {
        const { asFragment } = render(<ProductCard {...product} />);
        expect(asFragment()).toMatchSnapshot();
    });

    it('should render product image if imgUrl is provided', () => {
        const { getByAltText } = render(<ProductCard {...product} />);
        expect(getByAltText('Test Product')).toHaveAttribute('src', 'test.jpg');
    });

    it('should not render product image if imgUrl is not provided', () => {
        const productWithoutImg = { ...product, imgUrl: undefined };
        const { queryByAltText } = render(
            <ProductCard {...productWithoutImg} />
        );
        expect(queryByAltText('Test Product')).not.toBeInTheDocument();
    });
});
