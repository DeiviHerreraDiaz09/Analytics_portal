from django.test import TestCase, Client
from django.urls import reverse


class DashboardViewTests(TestCase):
    """
    Suite de pruebas para la vista del dashboard.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas.
        """
        self.client = Client()
        self.dashboard_url = reverse('dashboard')

    def test_dashboard_view_exists(self):
        """
        Verifica que la vista del dashboard exista y sea accesible.
        """
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_uses_correct_template(self):
        """
        Verifica que se use el template correcto.
        """
        response = self.client.get(self.dashboard_url)
        self.assertTemplateUsed(response, 'dashboard/index.html')

    def test_dashboard_contains_title(self):
        """
        Verifica que el contexto contenga el título correcto.
        """
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.context['title'], 'Portal Analítico')

    def test_dashboard_contains_analytics_data(self):
        """
        Verifica que los datos analíticos se pasen al contexto.
        """
        response = self.client.get(self.dashboard_url)
        self.assertIn('analytics_data', response.context)
        self.assertIsInstance(response.context['analytics_data'], list)
        self.assertGreater(len(response.context['analytics_data']), 0)

    def test_dashboard_analytics_data_structure(self):
        """
        Verifica que los datos tengan la estructura correcta.
        """
        response = self.client.get(self.dashboard_url)
        analytics_data = response.context['analytics_data']

        for record in analytics_data:
            self.assertIn('fecha', record)
            self.assertIn('cliente', record)
            self.assertIn('metrica', record)
            self.assertIn('valor', record)

    def test_html_contains_table(self):
        """
        Verifica que el HTML contenga una tabla.
        """
        response = self.client.get(self.dashboard_url)
        content = response.content.decode()
        self.assertIn('<table', content)
        self.assertIn('</table>', content)

    def test_html_contains_all_column_headers(self):
        """
        Verifica que la tabla contenga todos los encabezados.
        """
        response = self.client.get(self.dashboard_url)
        content = response.content.decode()
        self.assertIn('Fecha', content)
        self.assertIn('Cliente', content)
        self.assertIn('Métrica', content)
        self.assertIn('Valor', content)
