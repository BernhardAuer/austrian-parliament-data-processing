import azure from 'svelte-adapter-azure-swa';
import { vitePreprocess } from '@sveltejs/kit/vite';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: azure({
			customStaticWebAppConfig: {
				platform: {
					'apiRuntime': 'node:18'
				}
			}
		})
	},
	preprocess: vitePreprocess()
};

export default config;
