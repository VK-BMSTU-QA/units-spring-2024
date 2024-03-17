import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Category, PriceSymbol } from '../../types';

const mockProduct = {
    id: 1,
    name: 'Test Product',
    description: 'This is a test product',
    price: 100,
    priceSymbol: '$' as PriceSymbol,
    category: 'Одежда' as Category,
    imgUrl: 'test_image.jpg',
};

afterEach(jest.clearAllMocks);

describe('ProductCard test', () => {
    it('should render correctly', () => {
        const { asFragment } = render(<ProductCard {...mockProduct} />);
        expect(asFragment()).toMatchSnapshot();
    });

    it('should display product details correctly', () => {
        const { getByText, getByAltText } = render(
            <ProductCard {...mockProduct} />
        );

        expect(getByText('Test Product')).toBeInTheDocument();
        expect(getByText('This is a test product')).toBeInTheDocument();
        expect(getByText('100 $')).toBeInTheDocument();
        expect(getByText('Одежда')).toBeInTheDocument();
        expect(getByAltText('Test Product')).toBeInTheDocument();
    });

    it('should not render image if imgUrl is not provided', () => {
        const { queryByTestId } = render(
            <ProductCard {...mockProduct} imgUrl={undefined} />
        );

        expect(queryByTestId('product-image')).not.toBeInTheDocument();
    });
});
