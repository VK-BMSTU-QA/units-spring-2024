import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';

jest.mock('../../hooks', () => ({
    useProducts: jest.fn(() => [
        {
            id: 1,
            name: 'Product 1',
            description: 'Description 1',
            price: 100,
            priceSymbol: '$',
            category: 'Category 1',
            imgUrl: 'img1.png',
        },
        {
            id: 2,
            name: 'Product 2',
            description: 'Description 2',
            price: 200,
            priceSymbol: '$',
            category: 'Category 2',
            imgUrl: 'img2.png',
        },
    ]),
    useCurrentTime: jest.fn(() => '12:00 PM'),
}));

jest.mock('../../utils', () => ({
    applyCategories: jest.fn((products, categories) => products),
    updateCategories: jest.fn((selectedCategories, clickedCategory) => [
        ...selectedCategories,
        clickedCategory,
    ]),
    getPrice: jest.fn((price, priceSymbol) => `${price} ${priceSymbol}`),
}));

describe('MainPage test', () => {
    it('should render MainPage correctly', () => {
        const { getByText } = render(<MainPage />);
        expect(getByText('VK Маркет')).toBeInTheDocument();
        expect(getByText('12:00 PM')).toBeInTheDocument();
        expect(getByText('Product 1')).toBeInTheDocument();
        expect(getByText('Product 2')).toBeInTheDocument();
        expect(getByText('100 $')).toBeInTheDocument();
        expect(getByText('200 $')).toBeInTheDocument();
    });
});
