import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from '../../types';

afterEach(jest.clearAllMocks);
describe('Product card test', () => {
    it('should render correctly', () => {
        const products: Product = {
            id: 1,
            name: 'Название',
            description: 'Описание',
            price: 128,
            priceSymbol: '$',
            imgUrl: '',
            category: 'Одежда',
        };
        const rendered = render(<ProductCard {...products} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
});
