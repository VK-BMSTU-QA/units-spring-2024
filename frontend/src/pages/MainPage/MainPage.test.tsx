import { render, screen, fireEvent } from '@testing-library/react';
import { MainPage } from './MainPage';
import { act } from 'react-dom/test-utils';
import '@testing-library/jest-dom';
import { updateCategories } from '../../utils';

jest.mock('../../hooks', () => ({
    ...jest.requireActual('../../hooks'),
    useProducts: () => [
        {
            id: 1,
            name: 'Test Product 1',
            description: 'Description 1',
            price: 100,
            priceSymbol: '$',
            category: 'Electronics',
            imgUrl: 'test1.jpg',
        },
        {
            id: 2,
            name: 'Test Product 2',
            description: 'Description 2',
            price: 200,
            priceSymbol: '$',
            category: 'Clothing',
            imgUrl: 'test2.jpg',
        },
    ],
    useCurrentTime: () => '12:00 PM',
}));

jest.mock('../../utils', () => ({
    ...jest.requireActual('../../utils'),
    updateCategories: jest.fn(),
}));

describe('MainPage', () => {
    it('renders without errors', () => {
        act(() => {
            render(<MainPage />);
        });
    });

    it('displays current time', () => {
        render(<MainPage />);
        expect(screen.getByText('12:00 PM')).toBeInTheDocument();
    });

    it('displays categories', () => {
        render(<MainPage />);
        const categoryButton = screen.getByText('Электроника');
        expect(categoryButton).toBeInTheDocument();
    });

    it('adds category to selected categories on click', () => {
        render(<MainPage />);
        const categoryButton = screen.getByText('Электроника');
        fireEvent.click(categoryButton);
        expect(screen.queryByText('Test Product 2')).not.toBeInTheDocument();
        expect(updateCategories).toHaveBeenCalledWith([], 'Электроника');
    });

    it('calls setSelectedCategories with correct arguments on category click', () => {
        render(<MainPage />);
        const electronicsCategory = screen.getByText('Электроника');
        const clothingCategory = screen.getByText('Одежда');

        fireEvent.click(electronicsCategory);
        expect(updateCategories).toHaveBeenCalledWith([], 'Электроника');

        fireEvent.click(clothingCategory);
        expect(updateCategories).toHaveBeenCalledWith(
            ['Электроника'],
            'Одежда'
        );
    });
});
