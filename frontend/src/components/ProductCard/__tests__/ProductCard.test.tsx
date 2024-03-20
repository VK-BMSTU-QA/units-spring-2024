import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from '../ProductCard';
import { useProducts } from '../../../hooks';

afterEach(jest.clearAllMocks);
describe('ProductCard test', () => {
    it('should render correctly', () => {
        const products = useProducts();
        const rendered = render(<ProductCard key={products[0].id} {...products[0]} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
});
