import { fireEvent, render } from '@testing-library/react';
import { MainPage } from '../MainPage';
import { Category } from '../../../types/Category.js';
import { Product } from '../../../types/Product.js';
import { PriceSymbol } from '../../../types/Symbol.js';
import {applyCategories, updateCategories, getPrice } from '../../../utils';
import { useProducts, useCurrentTime } from '../../../hooks';



jest.mock('../../../hooks', () => ({
    useProducts: jest.fn(() => [
        {
            id: 1,
            name: 'One',
            description: 'number',
            price: 100,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '/pic.svg',
        },
        {
            id: 2,
            name: 'Two',
            description: 'number',
            price: 10000,
            priceSymbol: '₽',
            category: 'Одежда',
        },
    ]),
    useCurrentTime: jest.fn(() => '15:04:05'),
}));

jest.mock('../../../utils', () => ({
    applyCategories: jest.fn(
        (products: Product[], categories: Category[]) => products
    ),
    updateCategories: jest.fn(
        (currentCategories: Category[], currentCategory: Category) =>
            currentCategories
    ),
    getPrice: jest.fn((value: number, symbol: PriceSymbol) => '10000 ₽'),
}));

afterEach(jest.clearAllMocks);

describe('MainPage test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();

        expect(getPrice).toHaveBeenCalledTimes(2);
        expect(useProducts).toHaveBeenCalledTimes(1);
        expect(useCurrentTime).toHaveBeenCalledTimes(1);
        expect(applyCategories).toHaveBeenCalledTimes(1);
        expect(updateCategories).toHaveBeenCalledTimes(0);

    });
    it('should render correctly after click', () => {
        const rendered = render(<MainPage />);
        expect(updateCategories).toHaveBeenCalledTimes(0);
        fireEvent.click(
            rendered.getByText('Одежда', {
                selector: '.categories__badge',
            })
        );
        expect(updateCategories).toHaveBeenCalledTimes(1);
    });
});