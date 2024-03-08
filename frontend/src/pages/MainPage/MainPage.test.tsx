import { render, fireEvent } from '@testing-library/react';
import { MainPage } from './MainPage';
import { updateCategories } from '../../utils';

jest.mock('../../utils/updateCategories', () => ({
    updateCategories: jest.fn((currentCategories, changedCategory) => [
        ...currentCategories,
        changedCategory,
    ])
}));

beforeAll(() => {
    jest.useFakeTimers();
    jest.setSystemTime(new Date("07/03/2024 20:00"))
});

afterEach(jest.clearAllMocks);

afterAll(() => {
    jest.useRealTimers();
});

describe('MainPage test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
    it('should respond to click', () => {
        const rendered = render(<MainPage />);

        fireEvent.click(rendered.getByText('Одежда', {selector:'.categories__badge'}));

        expect(updateCategories).toHaveBeenCalled();
    });
});