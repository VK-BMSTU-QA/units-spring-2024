import { MainPage } from "./MainPage";
import { render, fireEvent } from "@testing-library/react";
import '@testing-library/jest-dom';
import * as currentTimeHook from "../../hooks/useCurrentTime"
import * as updateCategoriesModule from "../../utils/updateCategories"

const mockCurrentTime = jest.spyOn(currentTimeHook, 'useCurrentTime');
mockCurrentTime.mockReturnValue('15:39:10')

const mockUC = jest.spyOn(updateCategoriesModule, 'updateCategories')

afterEach(jest.clearAllMocks);
describe('Main page test', () => {
    it('should render', () => {
        const page = render(<MainPage/>);
        expect(page.asFragment()).toMatchSnapshot();
    });

    it('should call updateCategories', async () => {
        const page = render(<MainPage/>);
        const electronicButton = await page.findByTestId('pc-Электроника')
        expect(electronicButton).not.toBeUndefined;

        fireEvent.click(electronicButton!);
        expect(mockUC).toHaveBeenCalledTimes(1);
    });
});