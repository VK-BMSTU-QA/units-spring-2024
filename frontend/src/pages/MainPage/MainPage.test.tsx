import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import { MainPage } from './MainPage';
import { updateCategories } from '../../utils';
import '@testing-library/jest-dom/extend-expect';

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
    ]),
    useCurrentTime: jest.fn(() => '2024-03-09'),
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
    it('renders MainPage component correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.getByText('2024-03-09')).toBeInTheDocument();
        expect(rendered.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(
            rendered.getByText('Latest iphone, buy it now')
        ).toBeInTheDocument();
        expect(rendered.getByText('999 $')).toBeInTheDocument();

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('click function test', () => {
        const rendered = render(<MainPage />);

        const categoryButton = rendered.getByText('Электроника', {
            selector: '.categories__badge',
        });

        expect(updateCategories).toHaveBeenCalledTimes(0);

        fireEvent.click(categoryButton);

        expect(updateCategories).toHaveBeenCalledTimes(1);
    });
});
