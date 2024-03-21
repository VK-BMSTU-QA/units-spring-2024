import React from 'react';
import { Product } from '../../types';
import { ProductCard } from './ProductCard';
import { render } from '@testing-library/react';

describe('ProductCard test', () => {
    it('should render correctly', () => {
        const productProps: Product = {
            id: 100,
            name: 'Лаптоп',
            description: 'Лапотоп - это по русски ноутбук',
            price: 3000,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '/laptop.png',
        };

        const rendered = render(<ProductCard {...productProps} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
});
