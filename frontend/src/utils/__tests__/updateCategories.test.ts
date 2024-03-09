import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    it('should return categories with needed categories', () => {
        expect(
            updateCategories(['Одежда', 'Электроника'], 'Электроника')
        ).toStrictEqual(['Одежда']);
        expect(
            updateCategories(
                ['Одежда', 'Электроника', 'Для дома'],
                'Электроника'
            )
        ).toStrictEqual(['Одежда', 'Для дома']);
        expect(updateCategories(['Одежда'], 'Электроника')).toStrictEqual([
            'Одежда',
            'Электроника',
        ]);
        expect(updateCategories([], 'Электроника')).toStrictEqual([
            'Электроника',
        ]);
    });
});
