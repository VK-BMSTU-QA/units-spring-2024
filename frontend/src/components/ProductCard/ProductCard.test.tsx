import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from "./ProductCard";
import { Product } from '../../types/Product.js';

afterEach(jest.clearAllMocks);
describe('ProductCards test', () => {
    it('should render correctly', () => {
        const testProduct: Product = {
            id: 1,
            name: 'Test Product',
            description: 'This is a test description',
            price: 100,
            priceSymbol: '$',
            imgUrl: 'test-image-url.jpg',
            category: 'Для дома',
        };
        const rendered = render(<ProductCard {...testProduct} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
});
