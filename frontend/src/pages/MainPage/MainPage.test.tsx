import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { useCurrentTime } from '../../hooks';
import { updateCategories } from '../../utils';

afterEach(jest.clearAllMocks);

jest.mock('../../hooks/useCurrentTime', () => ({
    useCurrentTime: jest.fn(() => '00:00:00'),
}));

jest.mock('../../utils/updateCategories', () => ({
    updateCategories: jest.fn((selectedCategories, clickedCategory) => [
        ...selectedCategories,
        clickedCategory,
    ]),
}));

describe('MainPage test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
        expect(useCurrentTime).toHaveBeenCalledTimes(1);
    });

    it('should call updateCategories when category is selected', () => {
        const rendered = render(<MainPage />);
        const button = rendered.baseElement.getElementsByClassName('categories__badge')[0];
        expect(updateCategories).toHaveBeenCalledTimes(0);
        fireEvent.click(button);
        expect(updateCategories).toHaveBeenCalledTimes(1);
    });
});
