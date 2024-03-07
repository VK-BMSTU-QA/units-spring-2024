import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
// import { applyCategories } from '../../utils';
import { MainPage } from '../MainPage';

// jest.mock('../../utils');

afterEach(jest.clearAllMocks);
describe('MainPage test', () => {
    it('should render correctly', () => {
        // expect(applyCategories).toBeCalledTimes(0);
        const rendered = render(<MainPage />);
        // expect(applyCategories).toBeCalledTimes(1);
        // expect(applyCategories).toHaveBeenCalledWith([], []);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    // it('should add class for selected badge', () => {
    //     const rendered = render(<Categories selectedCategories={['Одежда']} />);

    //     expect(rendered.getByText('Одежда')).toHaveClass(
    //         'categories__badge_selected'
    //     );
    //     expect(rendered.getByText('Электроника')).not.toHaveClass(
    //         'categories__badge_selected'
    //     );
    //     expect(rendered.getByText('Для дома')).not.toHaveClass(
    //         'categories__badge_selected'
    //     );
    // });

    // it('should call callback when category click', () => {
    //     const onCategoryClick = jest.fn();
    //     const rendered = render(
    //         <Categories
    //             selectedCategories={[]}
    //             onCategoryClick={onCategoryClick}
    //         />
    //     );

    //     expect(onCategoryClick).toHaveBeenCalledTimes(0);
    //     fireEvent.click(rendered.getByText('Одежда'));
    //     expect(onCategoryClick).toHaveBeenCalledTimes(1);
    // });
});
