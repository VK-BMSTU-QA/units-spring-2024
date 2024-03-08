import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import { MainPage } from '../MainPage';
import { updateCategories } from '../../../utils';

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
    ]),
    useCurrentTime: jest.fn(() => '12:34:56'),
}));

jest.mock('../../../utils', () => ({
    ...jest.requireActual('../../../utils'),
    updateCategories: jest.fn(),
}));

describe('Main page test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('on click function is called', () => {
        const rendered = render(<MainPage />);

        const categoryButton = rendered.getByText('Одежда', {
            selector: '.categories__badge',
        });

        expect(updateCategories).toHaveBeenCalledTimes(0);

        fireEvent.click(categoryButton);

        expect(updateCategories).toHaveBeenCalledTimes(1);
    });
});
