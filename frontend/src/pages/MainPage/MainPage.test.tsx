import type { Category, Product, PriceSymbol } from '../../types';

jest.mock('../../hooks/useCurrentTime', () => ({
    useCurrentTime: () => '',
}));

jest.mock('../../hooks', () => ({
    useProducts: jest.fn(() => [
        {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '/iphone.png',
        },
        {
            id: 2,
            name: 'Костюм гуся',
            description: 'Запускаем гуся, работяги',
            price: 1000,
            priceSymbol: '₽',
            category: 'Одежда',
        },
    ]),
    useCurrentTime: jest.fn(() => ''),
}));

jest.mock('../../utils', () => ({
    applyCategories: jest.fn(
        (products: Product[], categories: Category[]) => products
    ),
    updateCategories: jest.fn(
        (currentCategories: Category[], currentCategory: Category) =>
            currentCategories
    ),
    getPrice: jest.fn((value: number, symbol: PriceSymbol) => '1000 ₽'),
}));

import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import React from 'react';

afterEach(jest.clearAllMocks);
describe('Product card test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
});
