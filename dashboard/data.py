from datetime import datetime, timedelta


def get_analytics_data():
    """
    Genera datos simulados de analítica.

    Returns:
        list: Lista de diccionarios con datos de cliente, fecha, métrica y valor.
    """
    base_date = datetime.now()

    data = [
        {
            'fecha': (base_date - timedelta(days=6)).strftime('%d/%m/%Y'),
            'cliente': 'Empresa A',
            'metrica': 'Visitantes',
            'valor': 1250,
        },
        {
            'fecha': (base_date - timedelta(days=6)).strftime('%d/%m/%Y'),
            'cliente': 'Empresa B',
            'metrica': 'Conversiones',
            'valor': 487,
        },
        {
            'fecha': (base_date - timedelta(days=5)).strftime('%d/%m/%Y'),
            'cliente': 'Empresa A',
            'metrica': 'Visitantes',
            'valor': 1680,
        },
        {
            'fecha': (base_date - timedelta(days=5)).strftime('%d/%m/%Y'),
            'cliente': 'Empresa C',
            'metrica': 'Click-Through Rate',
            'valor': 3.2,
        },
        {
            'fecha': (base_date - timedelta(days=4)).strftime('%d/%m/%Y'),
            'cliente': 'Empresa B',
            'metrica': 'Visitantes',
            'valor': 2145,
        },
        {
            'fecha': (base_date - timedelta(days=4)).strftime('%d/%m/%Y'),
            'cliente': 'Empresa C',
            'metrica': 'Conversiones',
            'valor': 652,
        },
        {
            'fecha': (base_date - timedelta(days=3)).strftime('%d/%m/%Y'),
            'cliente': 'Empresa A',
            'metrica': 'Conversiones',
            'valor': 542,
        },
        {
            'fecha': (base_date - timedelta(days=3)).strftime('%d/%m/%Y'),
            'cliente': 'Empresa B',
            'metrica': 'Click-Through Rate',
            'valor': 2.8,
        },
        {
            'fecha': (base_date - timedelta(days=2)).strftime('%d/%m/%Y'),
            'cliente': 'Empresa C',
            'metrica': 'Visitantes',
            'valor': 1890,
        },
        {
            'fecha': (base_date - timedelta(days=2)).strftime('%d/%m/%Y'),
            'cliente': 'Empresa A',
            'metrica': 'Click-Through Rate',
            'valor': 3.5,
        },
        {
            'fecha': (base_date - timedelta(days=1)).strftime('%d/%m/%Y'),
            'cliente': 'Empresa B',
            'metrica': 'Visitantes',
            'valor': 2320,
        },
        {
            'fecha': (base_date - timedelta(days=1)).strftime('%d/%m/%Y'),
            'cliente': 'Empresa C',
            'metrica': 'Conversiones',
            'valor': 718,
        },
        {
            'fecha': (base_date - timedelta(days=1)).strftime('%d/%m/%Y'),
            'cliente': 'Empresa D',
            'metrica': 'Visitantes',
            'valor': 1950,
        },
        {
            'fecha': (base_date - timedelta(days=1)).strftime('%d/%m/%Y'),
            'cliente': 'Empresa E',
            'metrica': 'Conversiones',
            'valor': 625,
        },
        {
            'fecha': (base_date - timedelta(days=1)).strftime('%d/%m/%Y'),
            'cliente': 'Empresa F',
            'metrica': 'Click-Through Rate',
            'valor': 2.1,
        }
    ]

    return data
