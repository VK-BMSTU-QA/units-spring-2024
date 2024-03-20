import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { useCurrentTime, useProducts } from '../../hooks';
import { applyCategories, updateCategories } from '../../utils';
import { Product, Category } from '../../types';


const products: Product[] = [
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
    {
        id: 3,
        name: 'Настольная лампа',
        description: 'Говорят, что ее использовали в pixar',
        price: 699,
        category: 'Для дома',
        imgUrl: '/lamp.png',
    },
    {
        id: 4,
        name: 'Принтер',
        description: 'Незаменимая вещь для студента',
        price: 7000,
        category: 'Электроника',
    },
]

jest.mock('../../hooks', () => ({
    useCurrentTime: jest.fn(() => '00:00:00'),
    useProducts: jest.fn(() => products)
}));

jest.mock('../../utils', () => ({
    applyCategories: jest.fn(() => [
        {
          id: 1,
          name: 'Телефон',
          description: 'Описание продукта 1',
          price: 100,
          category: 'Электроника'
        },
        {
          id: 4,
          name: 'Ноутбук',
          description: 'Описание продукта 4',
          price: 100,
          category: 'Электроника'
        }
      ]),
    getPrice:  jest.fn(),
    updateCategories: jest.fn(() => ['Одежда']),
}));

afterEach(jest.clearAllMocks);
describe('MainPage test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });


    it('should called categories butten after click', () => {
        const rendered = render(<MainPage />);
        expect(updateCategories).toHaveBeenCalledTimes(0);

        const categoryButton = rendered.getByText('Одежда', {
            selector: '.categories__badge',
        });
        fireEvent.click(categoryButton);
        expect(updateCategories).toHaveBeenCalledTimes(1);
    });

    it('should called when onload page', () => {
        render(<MainPage />);
        expect(useProducts).toHaveBeenCalledTimes(1);
        expect(useCurrentTime).toHaveBeenCalledTimes(1);
        expect(applyCategories).toHaveBeenCalledWith(products, []);
    });

});