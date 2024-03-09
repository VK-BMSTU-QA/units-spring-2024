import { MainPage } from "./MainPage";
import { render, fireEvent } from "@testing-library/react";
import '@testing-library/jest-dom';
import * as currentTimeHook from "../../hooks/useCurrentTime"
import * as updateCategoriesModule from "../../utils/updateCategories"
import * as applyCategoriesModule from "../../utils/applyCategories"

const mockCurrentTime = jest.spyOn(currentTimeHook, 'useCurrentTime');
mockCurrentTime.mockReturnValue('15:39:10')

const mockUC = jest.spyOn(updateCategoriesModule, 'updateCategories');
const mockAC = jest.spyOn(applyCategoriesModule, 'applyCategories');

afterEach(jest.clearAllMocks);
describe('Main page test', () => {
    it('should render correctly', () => {
        const page = render(<MainPage/>);
        expect(page.asFragment()).toMatchSnapshot();
    });

    it('should call updateCategories', async () => {
        const page = render(<MainPage/>);
        const electronicButton = await page.findByTestId('test-Электроника')
        expect(electronicButton).not.toBeUndefined;

        fireEvent.click(electronicButton!);
        expect(mockUC).toHaveBeenCalledTimes(1);
    });

    it('should call applyCategories', async () => {
        const page = render(<MainPage/>);

        const electronicButton = await page.findByTestId('test-Электроника')
        expect(electronicButton).not.toBeUndefined;

        expect(mockAC).toHaveBeenCalledTimes(1);

        expect(page.container.getElementsByClassName('categories__badge_selected')).toHaveLength(0);

        fireEvent.click(electronicButton);

        expect(mockAC).toHaveBeenCalledTimes(2);

        expect(page.container.getElementsByClassName('product-card')).toHaveLength(2);
        expect(page.container.getElementsByClassName('categories__badge_selected')).toHaveLength(1);

        expect(page.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(page.getByText('Принтер')).toBeInTheDocument();
        expect(page.queryByText('Костюм гуся')).not.toBeInTheDocument();
    });
});