import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from '../MainPage';
import { updateCategories } from '../../utils';
import { useCurrentTime, useProducts } from '../../hooks';

jest.mock('../../utils', () => ({
    applyCategories: jest.fn((products, categories) => products),
    getPrice: jest.fn((price, priceSymbol) => `${price} ${priceSymbol}`),
    updateCategories: jest.fn((selectedCategories, clickedCategory) => [
        ...selectedCategories,
        clickedCategory,
    ]),
}));


jest.mock('../../hooks', () => ({
    useCurrentTime: jest.fn(() => '00:00:00'),
    useProducts: jest.fn(() => [
        {
            id: 4,
            name: 'Принтер',
            description: 'Незаменимая вещь для студента',
            price: 7000,
            category: 'Электроника',
        },
    ]),
}));

afterEach(jest.clearAllMocks);


describe('Main page test', () => {

    it('should render correctly', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call callback when category click', () => {
        const rendered = render(<MainPage />);

        expect(updateCategories).toHaveBeenCalledTimes(0);
        rendered.getAllByText('Электроника').forEach((item) => {
            if(item.classList.contains('categories__badge')) {
                fireEvent.click(item);
            }
        });
        expect(updateCategories).toHaveBeenCalledTimes(1);
    });

});