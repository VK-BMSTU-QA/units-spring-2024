import { MainPage } from './MainPage';
import * as hooks from '../../hooks';
import * as utils from '../../utils';
import { Product } from '../../types/Product.js';
import { Category } from '../../types/Category.js';
import { fireEvent, getByText, render } from '@testing-library/react';
import { PriceSymbol } from '../../types/Symbol.js';

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
    useCurrentTime: jest.fn(() => '12:00:00'),
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

afterEach(jest.clearAllMocks);

describe('MainPage test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();

        expect(hooks.useProducts).toHaveBeenCalledTimes(1);
        expect(hooks.useCurrentTime).toHaveBeenCalledTimes(1);
        expect(utils.applyCategories).toHaveBeenCalledTimes(1);
        expect(utils.updateCategories).toHaveBeenCalledTimes(0);
        expect(utils.getPrice).toHaveBeenCalledTimes(2);
    });

    it('should render correctly with category on click', () => {
        const rendered = render(<MainPage />);
        expect(utils.updateCategories).toHaveBeenCalledTimes(0);
        fireEvent.click(
            rendered.getByText('Электроника', {
                selector: '.categories__badge',
            })
        );
        expect(utils.updateCategories).toHaveBeenCalledTimes(1);
    });
});
