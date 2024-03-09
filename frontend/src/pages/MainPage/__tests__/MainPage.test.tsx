import { render, fireEvent } from '@testing-library/react';
import { MainPage } from "../MainPage";
import { useCurrentTime, useProducts } from '../../../hooks';
import { applyCategories, updateCategories } from '../../../utils';
import '@testing-library/jest-dom';



jest.mock('../../../hooks', () => ({
    ...(jest.requireActual('../../../hooks')),
    useProducts: jest.fn(() => [
        {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '/iphone.png',
        },
        {
            id: 2,
            name: 'Костюм гуся',
            description: 'Запускаем гуся, работяги',
            price: 1000,
            priceSymbol: '₽',
            category: 'Одежда',
        },
        {
            id: 3,
            name: 'Настольная лампа',
            description: 'Говорят, что ее использовали в pixar',
            price: 699,
            category: 'Для дома',
            imgUrl: '/lamp.png',
        },
        {
            id: 4,
            name: 'Принтер',
            description: 'Незаменимая вещь для студента',
            price: 7000,
            category: 'Электроника',
        }
    ]),
    useCurrentTime: jest.fn(() => "12:00:00"),
}));

jest.mock('../../../utils', () => ({
    ...(jest.requireActual('../../../utils')),
    applyCategories: jest.fn((products, categories) => products),
    updateCategories: jest.fn((categories, changed) => [...categories, changed]),
    getPrice: jest.fn((price, priceSymbol) => `${price} ${priceSymbol}`),
}));

afterEach(jest.clearAllMocks);


describe('MainPage test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    test('should render all ProductCards for each product', async () => {
        const { getByText } = render(<MainPage />);

        expect(getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(getByText('Костюм гуся')).toBeInTheDocument();
        expect(getByText('Настольная лампа')).toBeInTheDocument();
        expect(getByText('Принтер')).toBeInTheDocument();
    });

    it('should call click handler when category clicked', () => {
        const rendered = render(<MainPage />);

        let category = rendered.getAllByText('Электроника')[0];

        expect(updateCategories).toHaveBeenCalledTimes(0);
        fireEvent.click(category);
        expect(updateCategories).toHaveBeenCalledTimes(1);

        expect(updateCategories).toHaveBeenCalledWith([], 'Электроника');

    });

    it('should call click handler when category clicked', () => {
        const rendered = render(<MainPage />);
        const category = rendered.getAllByText('Одежда')[0];

        expect(updateCategories).toHaveBeenCalledTimes(0);
        fireEvent.click(category);
        expect(updateCategories).toHaveBeenCalledTimes(1);
    
        expect(updateCategories).toHaveBeenCalledWith([], 'Одежда');
    });


});