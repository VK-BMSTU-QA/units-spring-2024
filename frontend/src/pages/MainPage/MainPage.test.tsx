import React from 'react';
import { render, fireEvent, getAllByText } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { updateCategories } from '../../utils';

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
    useCurrentTime: jest.fn(() => '15:42:50'),
}));

jest.mock('../../utils', () => ({
    applyCategories: jest.fn((products, categories) => products),
    updateCategories: jest.fn((selectedCategories, clickedCategory) => [
        ...selectedCategories,
        clickedCategory,
    ]),
    getPrice: jest.fn((price, priceSymbol) => `${price} ${priceSymbol}`),
}));

afterEach(jest.clearAllMocks);

describe('MainPage', () => {
    it('shouldrender', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call callback when category click', () => {
        const rendered = render(
            <MainPage/>
        );

        expect(updateCategories).toHaveBeenCalledTimes(0);
        fireEvent.click(rendered.getByText('Одежда', {selector: '.categories__badge'}));
        expect(updateCategories).toHaveBeenCalledTimes(1);
    });

});