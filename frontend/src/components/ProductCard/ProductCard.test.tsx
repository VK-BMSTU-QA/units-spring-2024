import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import type { Product } from '../../types';
import React from 'react';

afterEach(jest.clearAllMocks);
describe('Product card test', () => {
    it('should render correctly', () => {
        const product: Product = {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '/iphone.png',
        };

        const rendered = render(<ProductCard key={product.id} {...product} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
});
