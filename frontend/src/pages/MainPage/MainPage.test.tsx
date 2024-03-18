import { MainPage } from './MainPage';
import React from 'react';
import { applyCategories, updateCategories } from '../../utils';
import { useCurrentTime, useProducts } from '../../hooks';
import { Product } from '../../types';
import { fireEvent, render } from '@testing-library/react';

const testProducts: Product[] = [
    {
        id: 1,
        name: 'IPhone 14 Pro',
        description: 'Latest iphone, buy it now',
        price: 999,
        priceSymbol: '$',
        category: 'Электроника',
        imgUrl: '/iphone.png',
    },
];

jest.mock('../../utils/applyCategories', () => ({
    applyCategories: jest.fn(() => {
        return testProducts;
    }),
}));

jest.mock('../../utils/updateCategories', () => ({
    updateCategories: jest.fn(() => {
        return [];
    }),
}));

jest.mock('../../utils/getPrice', () => ({
    getPrice: jest.fn(() => ''),
}));

jest.mock('../../hooks/useCurrentTime', () => ({
    useCurrentTime: jest.fn(() => '12:00:00'),
}));

jest.mock('../../hooks/useProducts', () => ({
    useProducts: jest.fn(() => {
        return testProducts;
    }),
}));

afterEach(jest.clearAllMocks);
describe('MainPage test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should update feed after click on category', () => {
        const rendered = render(<MainPage />);

        fireEvent.click(rendered.getByText('Одежда'));
        expect(updateCategories).toHaveBeenCalledWith([], 'Одежда');
    });

    it('should call callbacks', () => {
        render(<MainPage />);

        expect(useProducts).toHaveBeenCalledTimes(1);
        expect(useCurrentTime).toHaveBeenCalledTimes(1);
        expect(applyCategories).toHaveBeenCalledTimes(1);
        expect(updateCategories).toHaveBeenCalledTimes(0);
    });

    it('should render the title, correct number of products, time', () => {
        const expectedProductsCount = 1;

        const { getByText } = render(<MainPage />);

        const titleElement = getByText('VK Маркет');
        const timeElement = getByText('12:00:00');
        const productCardElements = document.getElementsByClassName('product-card');

        expect(titleElement).toBeTruthy();
        expect(timeElement).toBeTruthy();
        expect(productCardElements).toHaveLength(expectedProductsCount);
    });
});
