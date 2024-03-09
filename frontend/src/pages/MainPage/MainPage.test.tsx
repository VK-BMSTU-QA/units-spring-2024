import React from 'react';
import { fireEvent, render, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { updateCategories } from '../../utils';

jest.mock('../../hooks', () => ({
    useProducts: jest.fn(() => [
        {
            id: 1,
            name: 'q',
            category: 'Одежда',
            description: 'q',
            imgUrl: '1',
            price: 100,
            priceSymbol: '₽',
        },
        {
            id: 2,
            name: 'q',
            category: 'Для дома',
            description: 'q',
            imgUrl: '1',
            price: 100,
            priceSymbol: '₽',
        },
        {
            id: 3,
            name: 'q',
            category: 'Электроника',
            description: 'q',
            imgUrl: '1',
            price: 100,
            priceSymbol: '₽',
        },
    ]),
    useCurrentTime: jest.fn(() => '01:23:45'),
}));

jest.mock('../../utils', () => ({
    applyCategories: jest.fn(() => []),
    updateCategories: jest.fn((currentCategories, changedCategory) => [
        ...currentCategories,
        changedCategory,
    ]),
}));

afterEach(jest.clearAllMocks);

describe('MainPage test', () => {
    it('should render correctly', async () => {
        const { asFragment } = render(<MainPage />);
        await waitFor(() => {
            expect(asFragment()).toMatchSnapshot();
        });
    });

    it('should render correct title and time', async () => {
        const { getByText } = render(<MainPage />);
        await waitFor(() => {
            expect(getByText('VK Маркет')).toBeInTheDocument();
            expect(getByText('01:23:45')).toBeInTheDocument();
        });
    });

    it('should work out the functions correctly', () => {
        const rendered = render(<MainPage />);
        const categoryButton = rendered.getByText('Одежда', {
            selector: '.categories__badge',
        });
        expect(updateCategories).toHaveBeenCalledTimes(0);
        fireEvent.click(categoryButton);
        expect(updateCategories).toHaveBeenCalledTimes(1);
    });
});
