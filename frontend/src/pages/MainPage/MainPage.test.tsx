import { render, screen, fireEvent } from '@testing-library/react';
import { createRoot } from 'react-dom/client';
import { MainPage } from './MainPage';
import { act } from 'react-dom/test-utils';
import '@testing-library/jest-dom';
import {updateCategories} from "../../utils";

jest.mock('../../hooks', () => ({
    ...jest.requireActual('../../hooks'), // Импортируем все остальные хуки как обычно
    useCurrentTime: () => '12:00 PM',
}));

describe('MainPage', () => {
    it('renders without errors', () => {
        act(() => {
            render(<MainPage />);
        });
    });

    it('displays categories', () => {
        expect(
            render(<MainPage />).container.querySelector('.categories__badge')
        ).toBeInTheDocument();
    });

    it('adds category to selected categories on click', () => {
        render(<MainPage />);
        const categoryButton = screen.getByText('Электроника', { selector: '.categories__badge' });
        expect(categoryButton).toBeInTheDocument();

        fireEvent.click(categoryButton);

        const excludedProduct = screen.queryByText('Костюм гуся');
        expect(excludedProduct).not.toBeInTheDocument();
    });
});