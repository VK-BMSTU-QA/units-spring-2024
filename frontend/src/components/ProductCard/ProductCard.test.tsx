import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { useProducts } from '../../hooks';

const products = useProducts();

afterEach(jest.clearAllMocks);
describe('ProductCard test', () => {
    it('should render correctly', () => {
        const rendered = render(<ProductCard {...products[0]} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should be all properties', () => {
        const rendered = render(<ProductCard {...products[0]} />);

        expect(rendered.getByText('IPhone 14 Pro')).toBeTruthy();

        expect(rendered.getByText('Latest iphone, buy it now')).toHaveClass(
            'product-card__description'
        );
    });
});
