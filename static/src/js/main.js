import axios from "axios";
import { createApp, h } from "vue";

import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/aura';

import { createInertiaApp } from "@inertiajs/vue3";

axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = "csrftoken"

createInertiaApp({
  resolve: (name) => {
    const pages = import.meta.glob("./Pages/**/*.vue", { eager: true });
    return pages[`./Pages/${name}.vue`];
  },
  setup({ el, App, props, plugin }) {
    createApp({ render: () => h(App, props) })
      .use(plugin)
      .use(PrimeVue, {
        theme: {
          preset: Aura
        }
      })
      .mount(el);
  },
});
