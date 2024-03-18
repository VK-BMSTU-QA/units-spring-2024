import { render, fireEvent } from '@testing-library/react';
import { MainPage } from './MainPage';
import { updateCategories } from '../../utils';

const testDate = "07/03/2024";
const testTime = "20:00:00";
const expectedProducts = 4;

jest.mock('../../utils/updateCategories', () => ({
    updateCategories: jest.fn((currentCategories, changedCategory) => [
        ...currentCategories,
        changedCategory,
    ])
}));

beforeAll(() => {
    jest.useFakeTimers();
    jest.setSystemTime(new Date(testDate + " " +testTime));
});

afterEach(jest.clearAllMocks);

afterAll(() => {
    jest.useRealTimers();
});

describe('MainPage test', () => {
    it('should render', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
    it('should render header', () => {
        const rendered = render(<MainPage />);
        
        expect(rendered.container.getElementsByClassName('main-page__title')).toHaveLength(1);
    });
    it('should render time', () => {
        const rendered = render(<MainPage />);
        
        expect(rendered.queryByText(testTime)?.textContent).toEqual(testTime);
    });
    it('should render the correct amount of products', () => {
        const rendered = render(<MainPage />);
        
        expect(rendered.container.getElementsByClassName('product-card')).toHaveLength(expectedProducts);
    });
    it('should respond to click', () => {
        const rendered = render(<MainPage />);

        const button = rendered.getByText('Одежда', {selector:'.categories__badge'});
        expect(button.classList.contains('categories__badge_selected')).toBe(false);

        fireEvent.click(button);

        expect(updateCategories).toHaveBeenCalled();
        expect(button.classList.contains('categories__badge_selected')).toBe(true);
    });
});
