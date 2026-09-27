<template>
  <header class="navbar" :class="{ scrolled: isScrolled, 'menu-open': menuOpen }">
    <div class="container navbar-inner">
      <!-- Logo -->
      <router-link to="/" class="navbar-logo" @click="closeMenu" aria-label="Bosh sahifa">
        <img v-if="logoUrl" :src="logoUrl" alt="Hackathon IT School Logo" class="navbar-custom-logo" />
        <div v-else class="logo-text-group">
          <span class="navbar-logo-text">{{ siteTitle || 'HACKATHON' }}</span>
          <span class="navbar-logo-sub font-mono">IT SCHOOL</span>
        </div>
      </router-link>

      <!-- Desktop Navigation -->
      <nav class="navbar-nav" aria-label="Asosiy navigatsiya">
        <router-link to="/" class="nav-link">Bosh sahifa</router-link>
        <a href="#olimpiada" class="nav-link">Olimpiada</a>
        <a href="#natijalar" class="nav-link">Sertifikatlar</a>
        <a href="#maktab" class="nav-link">Maktab haqida</a>
        <a href="#yonalishlar" class="nav-link">Yo'nalishlar</a>
      </nav>

      <!-- CTA + Mobile Toggle -->
      <div class="navbar-actions">
        <router-link to="/register" class="btn-editorial-pill btn-nav-cta">
          <span>Qatnashish</span>
          <span>→</span>
        </router-link>
        <button
          class="hamburger"
          @click="toggleMenu"
          :aria-expanded="menuOpen"
          aria-label="Menyu"
        >
          <span class="hamburger-line"></span>
          <span class="hamburger-line"></span>
          <span class="hamburger-line"></span>
        </button>
      </div>
    </div>

    <!-- Mobile Menu -->
    <transition name="mobile-menu">
      <div v-if="menuOpen" class="mobile-menu">
        <nav class="mobile-nav" aria-label="Mobil navigatsiya">
          <router-link to="/" class="mobile-nav-link" @click="closeMenu">Bosh sahifa</router-link>
          <a href="#olimpiada" class="mobile-nav-link" @click="closeMenu">Olimpiada</a>
          <a href="#natijalar" class="mobile-nav-link" @click="closeMenu">Sertifikatlar</a>
          <a href="#maktab" class="mobile-nav-link" @click="closeMenu">Maktab haqida</a>
          <a href="#yonalishlar" class="mobile-nav-link" @click="closeMenu">Yo'nalishlar</a>
          <router-link to="/register" class="btn-editorial-pill mobile-cta" @click="closeMenu">
            <span>Ro'yxatdan o'tish</span>
            <span>→</span>
          </router-link>
        </nav>
      </div>
    </transition>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { getSiteSettings } from '../services/api.js'

const isScrolled = ref(false)
const menuOpen = ref(false)
const logoUrl = ref('')
const siteTitle = ref('')

function handleScroll() {
  isScrolled.value = window.scrollY > 20
}

function toggleMenu() {
  menuOpen.value = !menuOpen.value
  document.body.style.overflow = menuOpen.value ? 'hidden' : ''
}

function closeMenu() {
  menuOpen.value = false
  document.body.style.overflow = ''
}

onMounted(async () => {
  window.addEventListener('scroll', handleScroll, { passive: true })
  handleScroll()

  const settings = await getSiteSettings()
  if (settings) {
    if (settings.logo_url) logoUrl.value = settings.logo_url
    if (settings.site_name) siteTitle.value = settings.site_name
  }
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  document.body.style.overflow = ''
})
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  height: var(--header-height);
  transition: all 0.3s ease;
  border-bottom: 1px solid transparent;
  background: transparent;
}

.navbar-custom-logo {
  max-height: 44px;
  max-width: 160px;
  object-fit: contain;
}

.navbar.scrolled {
  background: rgba(6, 8, 20, 0.85);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom-color: var(--border-subtle);
}

.navbar-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
}

.navbar-logo {
  display: flex;
  align-items: center;
  z-index: 10;
}

.logo-text-group {
  display: flex;
  flex-direction: column;
}

.navbar-logo-text {
  font-weight: 800;
  font-size: 1.1rem;
  letter-spacing: -0.02em;
  color: #ffffff;
  line-height: 1;
}

.navbar-logo-sub {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: var(--gold);
}

.navbar-nav {
  display: flex;
  align-items: center;
  gap: 36px;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}

.nav-link {
  font-size: 0.88rem;
  font-weight: 500;
  color: var(--text-secondary);
  transition: color 0.2s;
}

.nav-link:hover {
  color: #ffffff;
}

.navbar-actions {
  display: flex;
  align-items: center;
  gap: 16px;
}

.btn-nav-cta {
  padding: 8px 18px;
  font-size: 0.85rem;
}

.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  padding: 8px;
  background: none;
  border: none;
  cursor: pointer;
  z-index: 10;
}

.hamburger-line {
  width: 22px;
  height: 1.5px;
  background: var(--text-main);
  transition: all 0.3s;
}

.menu-open .hamburger-line:nth-child(1) {
  transform: rotate(45deg) translate(4.5px, 4.5px);
}
.menu-open .hamburger-line:nth-child(2) {
  opacity: 0;
}
.menu-open .hamburger-line:nth-child(3) {
  transform: rotate(-45deg) translate(4.5px, -4.5px);
}

/* Mobile Menu */
.mobile-menu {
  position: fixed;
  inset: 0;
  top: var(--header-height);
  background: rgba(6, 8, 20, 0.98);
  backdrop-filter: blur(14px);
  z-index: 999;
  display: flex;
  flex-direction: column;
  padding: 48px 32px;
}

.mobile-nav {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.mobile-nav-link {
  font-size: 1.25rem;
  font-weight: 500;
  color: var(--text-secondary);
  transition: color 0.2s;
}

.mobile-nav-link:hover {
  color: #ffffff;
}

.mobile-cta {
  margin-top: 20px;
  width: max-content;
}

.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: opacity 0.3s, transform 0.3s;
}
.mobile-menu-enter-from,
.mobile-menu-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

@media (max-width: 860px) {
  .navbar-nav {
    display: none;
  }
  .btn-nav-cta {
    display: none;
  }
  .hamburger {
    display: flex;
  }
}
</style>
