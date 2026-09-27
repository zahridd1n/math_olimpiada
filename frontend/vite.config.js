import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5173,
    host: true,
  },
  build: {
    target: 'es2020',
    minify: 'esbuild',
  },
})
