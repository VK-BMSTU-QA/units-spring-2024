import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { useProducts } from '../../hooks';

afterEach(jest.clearAllMocks);
describe('test ProductCard', () => {
    it('should render correctly', () => {
        const product = useProducts()[0];
        const rendered = render(<ProductCard {...product} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });
});
