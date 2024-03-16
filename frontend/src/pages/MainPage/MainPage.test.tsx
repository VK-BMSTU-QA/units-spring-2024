import React from 'react';
import { fireEvent, render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { updateCategories } from '../../utils';

jest.mock('../../hooks', () => ({
    useProducts: jest.fn(() => [
        {
            id: 1,
            name: '1',
            description: '1',
            price: 1,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '1.png',
        },
        {
            id: 2,
            name: '2',
            description: '2',
            price: 2,
            priceSymbol: '$',
            category: 'Для дома',
            imgUrl: '2.png',
        },
    ]),
    useCurrentTime: jest.fn(() => '17:51:39'),
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
    it('should render correctly', () => {
        const rendered =  render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should have correct render text', () => {
        const rendered =  render(<MainPage />);

        expect(rendered.getByText('VK Маркет')).toBeInTheDocument();
        expect(rendered.getByText('17:51:39')).toBeInTheDocument();
    });

    it('should work out the functions correctly', () => {
        const rendered = render(<MainPage />);

        const categoryButton = rendered.getByText('Электроника', {
            selector: '.categories__badge',
        });

        expect(updateCategories).toHaveBeenCalledTimes(0);

        fireEvent.click(categoryButton);

        expect(updateCategories).toHaveBeenCalledTimes(1);
        expect(categoryButton.classList.contains('categories__badge_selected')).toBeTruthy();
    });
});
