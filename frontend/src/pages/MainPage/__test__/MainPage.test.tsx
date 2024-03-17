import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import '@testing-library/jest-dom';

import { MainPage } from '../MainPage';
import { applyCategories, updateCategories } from '../../../utils';

jest.mock('../../../hooks', () => ({
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
      {
        id: 3,
        name: 'Настольная лампа',
        description: 'Говорят, что ее использовали в pixar',
        price: 699,
        priceSymbol: '₽',
        category: 'Для дома',
        imgUrl: '/lamp.png',
      },
      {
        id: 4,
        name: 'Принтер',
        description: 'Незаменимая вещь для студента',
        price: 7000,
        priceSymbol: '₽',
        category: 'Электроника',
      },
    ]),
    useCurrentTime: jest.fn(() => '12:00 PM'),
}));

jest.mock('../../../utils', () => ({
    applyCategories: jest.fn((products, categories) => products),
    updateCategories: jest.fn((selectedCategories, clickedCategory) => [
        ...selectedCategories,
        clickedCategory,
    ]),
    getPrice: jest.fn((price, priceSymbol) => `${price} ${priceSymbol}`),
}));

describe('MainPage', () => {
    test('renders MainPage component', () => {
        const { getByText } = render(<MainPage />);
        expect(getByText('VK Маркет')).toBeInTheDocument();
        expect(getByText('12:00 PM')).toBeInTheDocument();
    });

    test('renders ProductCard for each product', async () => {
        const { getByText } = render(<MainPage />);

        expect(getByText('Принтер')).toBeInTheDocument();
        expect(getByText('Настольная лампа')).toBeInTheDocument();
        expect(getByText('Костюм гуся')).toBeInTheDocument();
        expect(getByText('IPhone 14 Pro')).toBeInTheDocument();
    });

    test('handles category click', () => {
      const { getByText } = render(<MainPage />);

      const categoryElements = screen.getAllByText('Для дома');

      fireEvent.click(categoryElements[0]);

      const mock = [
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
          priceSymbol: '₽',
          category: 'Для дома',
          imgUrl: '/lamp.png',
        },
        {
          id: 4,
          name: 'Принтер',
          description: 'Незаменимая вещь для студента',
          price: 7000,
          priceSymbol: '₽',
          category: 'Электроника',
        },
      ];
        
      expect(updateCategories).toHaveBeenNthCalledWith(1, [], 'Для дома');
      expect(updateCategories).toHaveBeenCalledTimes(1);
      expect(applyCategories).toHaveBeenNthCalledWith(4, mock, ['Для дома']); // len(mock) = 4
      expect(applyCategories).toHaveBeenCalledTimes(4);
    });
});
