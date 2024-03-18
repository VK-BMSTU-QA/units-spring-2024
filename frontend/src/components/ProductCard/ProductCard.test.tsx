import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import type { Product } from '../../types';
import { getPrice } from '../../utils';


afterEach(jest.clearAllMocks);
jest.mock('../../utils', () => ({
    ...(jest.requireActual('../../utils')),
    getPrice: jest.fn(() => '300 $'),
}));
describe('ProductCard test', () => {
    it('should render correctly', () => {
        const prod: Product = {
            id: 1,
            name: 'пельмени',
            description: 'вкусняшка',
            price: 300,
            priceSymbol: '$',
            category: 'Для дома',
        };
        const rendered = render(<ProductCard key={prod.id} {...prod} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should add class for name, description, price elements', () => {
        const prod: Product = {
            id: 1,
            name: 'пельмени',
            description: 'вкусняшка',
            price: 300,
            priceSymbol: '$',
            category: 'Для дома',
        };
        const rendered = render(<ProductCard key={prod.id} {...prod} />);

        expect(rendered.getByText('пельмени')).toHaveClass(
            'product-card__name'
        );
        expect(rendered.getByText('вкусняшка')).toHaveClass(
            'product-card__description'
        );
        expect(rendered.getByText('300 $')).toHaveClass(
            'product-card__price'
        );
        expect(rendered.getByText('Для дома')).toHaveClass(
            'product-card__category'
        );
    });

    it('should make name, description, price elements visible', () => {
        const prod: Product = {
            id: 1,
            name: 'пельмени',
            description: 'вкусняшка',
            price: 300,
            priceSymbol: '$',
            category: 'Для дома',
        };
        const rendered = render(<ProductCard key={prod.id} {...prod} />);

        expect(rendered.getByText('пельмени')).toBeVisible();
        expect(rendered.getByText('вкусняшка')).toBeVisible();
        expect(rendered.getByText('300 $')).toBeVisible();
    });

    it('should not render image if no url provided', () => {
        const prod: Product = {
            id: 1,
            name: 'пельмени',
            description: 'вкусняшка',
            price: 300,
            priceSymbol: '$',
            category: 'Для дома',
        };
        const rendered = render(<ProductCard key={prod.id} {...prod} />);

        expect(rendered.queryByAltText('пельмени')).toBeNull();
    });

    it('should add image with required class', () => {
        const prod: Product = {
            id: 1,
            name: 'пельмени',
            description: 'вкусняшка',
            price: 300,
            priceSymbol: '$',
            category: 'Для дома',
            imgUrl: 'public/lamp.png'
        };
        const rendered = render(<ProductCard key={prod.id} {...prod} />);

        expect(rendered.getByAltText('пельмени')).toHaveClass(
            'product-card__image'
        );
        expect(rendered.getByText('пельмени')).toBeVisible();
        expect(getPrice).toBeCalledTimes(1);
    });
});

