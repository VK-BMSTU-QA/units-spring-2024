import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { updateCategories } from '../../utils';

jest.mock('../../hooks', () => ({
    useProducts: jest.fn(() => [
        {
            id: 2,
            name: 'Костюм гуся',
            description: 'Запускаем гуся, работяги',
            price: 1000,
            priceSymbol: '₽',
            category: 'Одежда',
        },
        {
            id: 3,
            name: 'Настольная лампа',
            description: 'Говорят, что ее использовали в pixar',
            price: 699,
            category: 'Для дома',
            imgUrl: '/lamp.png',
        },
    ]),
    useCurrentTime: jest.fn(() => '11:11:11'),
}));

jest.mock('../../utils', () => ({
    applyCategories: jest.fn((products) => products),
    updateCategories: jest.fn((selectedCategories, clickedCategory) => [
        ...selectedCategories,
        clickedCategory,
    ]),
    getPrice: jest.fn((price, priceSymbol) => `${price} ${priceSymbol}`),
}));

afterEach(jest.clearAllMocks);

describe('MainPage', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render header', () => {
        const { container } = render(<MainPage />);
        const headerElement =
            container.getElementsByClassName('main-page__title');
        const categoriesElement =
            container.getElementsByClassName('categories__badge');

        expect(headerElement.length).toBe(1);
        expect(categoriesElement.length).toBe(3);
    });

    it('should render current time', () => {
        const { getByText } = render(<MainPage />);
        const timeElement = getByText(/\d{2}:\d{2}:\d{2}/);

        expect(timeElement).toBeInTheDocument();
    });

    it('should render expected number of products', () => {
        const { container } = render(<MainPage />);
        const productElements =
            container.getElementsByClassName('product-card');

        expect(productElements).toHaveLength(2);
    });

    it('should render correctly with category on click', () => {
        const rendered = render(<MainPage />);

        const categoryButton = rendered.getByText('Одежда', {
            selector: '.categories__badge',
        });

        expect(updateCategories).toHaveBeenCalledTimes(0);
        expect(categoryButton).not.toHaveClass('categories__badge_selected');
        fireEvent.click(categoryButton);
        expect(updateCategories).toHaveBeenCalledTimes(1);
        expect(categoryButton).toHaveClass('categories__badge_selected');
    });
});
