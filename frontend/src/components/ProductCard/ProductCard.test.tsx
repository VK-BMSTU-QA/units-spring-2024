import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import type { Product } from '../../types';
import { getPrice } from '../../utils';


afterEach(jest.clearAllMocks);
jest.mock('../../utils', () => ({
    ...(jest.requireActual('../../utils')),
    getPrice: jest.fn(() => '420 ₽'),
}));
describe('ProductCard test', () => {
    it('should render correctly', () => {
        const prod: Product = {
            id: 1,
            name: 'pelmeni',
            description: 'floppa',
            price: 420,
            priceSymbol: '₽',
            category: 'Электроника',
        };
        const rendered = render(<ProductCard key={prod.id} {...prod} />);
        
        expect(rendered.asFragment()).toMatchSnapshot();
    });
    
    it('should add class for name, description, price elements', () => {
        const prod: Product = {
            id: 1,
            name: 'pelmeni',
            description: 'floppa',
            price: 420,
            priceSymbol: '₽',
            category: 'Электроника',
        };
        const rendered = render(<ProductCard key={prod.id} {...prod} />);

        expect(rendered.getByText('pelmeni')).toHaveClass(
            'product-card__name'
        );
        expect(rendered.getByText('floppa')).toHaveClass(
            'product-card__description'
        );
        expect(rendered.getByText('420 ₽')).toHaveClass(
            'product-card__price'
        );
    });

    it('should make name, description, price elements visible', () => {
        const prod: Product = {
            id: 1,
            name: 'pelmeni',
            description: 'floppa',
            price: 420,
            priceSymbol: '₽',
            category: 'Электроника',
        };
        const rendered = render(<ProductCard key={prod.id} {...prod} />);

        expect(rendered.getByText('pelmeni')).toBeVisible();
        expect(rendered.getByText('floppa')).toBeVisible();
        expect(rendered.getByText('420 ₽')).toBeVisible();
    });

    it('should not render image if no url provided', () => {
        const prod: Product = {
            id: 1,
            name: 'pelmeni',
            description: 'floppa',
            price: 420,
            priceSymbol: '₽',
            category: 'Электроника',
        };
        const rendered = render(<ProductCard key={prod.id} {...prod} />);

        expect(rendered.queryByAltText('pelmeni')).toBeNull();
    });

    it('should add image with required class', () => {
        const prod: Product = {
            id: 1,
            name: 'pelmeni',
            description: 'floppa',
            price: 420,
            priceSymbol: '₽',
            category: 'Электроника',
            imgUrl: '/sirniki.png',
        };
        const rendered = render(<ProductCard key={prod.id} {...prod} />);

        expect(rendered.getByAltText('pelmeni')).toBeVisible();
        expect(rendered.getByAltText('pelmeni')).toHaveClass(
            'product-card__image'
        );
    });
});
