import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';

jest.mock('../../utils/updateCategories');
import { updateCategories } from '../../utils/updateCategories';

afterEach(jest.clearAllMocks);
describe('Main page test', () => {
    beforeAll(() => {
        jest.useFakeTimers();
        jest.setSystemTime(new Date('20 Aug 2020 02:12:00').getTime())
      });

    afterAll(() => {
        jest.useRealTimers();
    });

    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call callback when category click', () => {
        const rendered = render(
            <MainPage />
        );

        expect(updateCategories).toHaveBeenCalledTimes(0);
        rendered.getAllByText('Одежда').forEach((item) => {
            if(item.classList.contains('categories__badge')) {
                fireEvent.click(item);
            }
        });
        expect(updateCategories).toHaveBeenCalledTimes(1);
    });

});
