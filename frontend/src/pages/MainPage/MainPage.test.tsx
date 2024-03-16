import React from 'react';
import { fireEvent, queryAllByText, queryByAltText, render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { applyCategories, getPrice, updateCategories } from '../../utils';
import { useCurrentTime, useProducts } from '../../hooks';
import { Product } from '../../types';

const products: Product[] = [
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
        priceSymbol: '₽',
        category: 'Для дома',
    }
];

jest.mock('../../hooks', () => ({
    useProducts: jest.fn(() => products),
    useCurrentTime: jest.fn(() => '4:20:00'),
}));

jest.mock('../../utils', () => ({
    applyCategories: jest.fn((products, categories) => products),
    updateCategories: jest.fn((selectedCategories, clickedCategory) => [
        ...selectedCategories,
        clickedCategory,
    ]),
    getPrice: jest.fn((price, priceSymbol) => `${price} ${priceSymbol}`),
}));

describe('test MainPage component', () => {

    it('should render correctly', () => {
        const rendered =  render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should have correct header and time', () => {
        const rendered =  render(<MainPage />);

        expect(rendered.getByText('VK Маркет')).toBeInTheDocument();
        expect(rendered.getByText('4:20:00')).toBeInTheDocument();
    });

    it('should call functions', () => {
        render(<MainPage />);

        expect(useProducts).toHaveBeenCalled();
        expect(useCurrentTime).toHaveBeenCalled();
        expect(getPrice).toBeCalledWith(products[0].price, products[0].priceSymbol);
        expect(getPrice).toBeCalledWith(products[1].price, products[1].priceSymbol);
        expect(applyCategories).toHaveBeenCalledWith(products, []);
    });

    it('shoudld call update and apply Categories on click', () => {
        const rendered = render(<MainPage />);

        const categoryButton = rendered.getByText('Электроника', {
            selector: '.categories__badge',
        });

        expect(updateCategories).toHaveBeenCalledTimes(0);

        fireEvent.click(categoryButton);

        expect(rendered.getByText('Электроника', { selector: '.categories__badge_selected',})).toBeInTheDocument();
        expect(applyCategories).toBeCalled();
        expect(updateCategories).toHaveBeenCalledTimes(1);
        expect(updateCategories).toHaveBeenCalledWith([], 'Электроника');
    });
});
