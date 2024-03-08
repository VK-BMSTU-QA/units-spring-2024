import { render } from '@testing-library/react';
import { ProductCard } from './ProductCard';
import { Product } from '../../types/Product';
import { getPrice } from '../../utils';

const testProduct: Product = {id: 1, name: 'Aspire ES 15', description: 'Ноутбук', price: 100, category: 'Электроника'}

jest.mock('../../utils/getPrice', () => ({
    getPrice: jest.fn()
}));

afterEach(jest.clearAllMocks);

describe('Categories test', () => {
    it('should render correctly', () => {
        const rendered = render(<ProductCard
            {...testProduct}
            priceSymbol='₽'
             />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
    it('should call getPrice when rendering', () => {
        expect(getPrice).toHaveBeenCalledTimes(0);

        const rendered = render(<ProductCard
            {...testProduct}
            priceSymbol='₽'
             />);

        expect(getPrice).toHaveBeenCalledTimes(1);
    });
});
