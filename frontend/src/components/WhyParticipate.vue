<template>
  <section class="section">
    <div class="container">
      <div class="section-header reveal" ref="headerRef">
        <h2 class="section-title">Nima uchun ishtirok etish kerak?</h2>
        <p class="section-subtitle">
          Olimpiadada qatnashish orqali siz quyidagi imkoniyatlarga ega bo'lasiz.
        </p>
      </div>

      <div class="why-grid reveal" ref="gridRef">
        <div v-for="(item, i) in reasons" :key="i" class="why-card" :class="'delay-' + (i+1)">
          <div class="why-header">
            <div class="why-icon-wrapper" :class="{ 'blue': i % 2 !== 0 }">
              <component :is="item.icon" class="why-icon" />
            </div>
            <span class="why-number">0{{ i + 1 }}</span>
          </div>
          <h3 class="why-title">{{ item.title }}</h3>
          <p class="why-desc">{{ item.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { siteConfig } from '../config/site.js'

const reasons = siteConfig.whyParticipate
const headerRef = ref(null)
const gridRef = ref(null)

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active')
      }
    })
  }, { threshold: 0.1 })

  if (headerRef.value) observer.observe(headerRef.value)
  if (gridRef.value) observer.observe(gridRef.value)
})
</script>

<style scoped>
.why-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.why-grid.active .why-card {
  animation: fadeUp 0.6s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

.why-card {
  padding: 32px 24px;
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-xl);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  opacity: 0;
  transform: translateY(20px);
}

.why-card:hover {
  border-color: var(--border-hover);
  background: var(--bg-card-hover);
  transform: translateY(-6px);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.3);
}

.why-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 32px;
}

.why-icon-wrapper {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: rgba(245, 197, 24, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.why-icon-wrapper.blue {
  background: rgba(59, 130, 246, 0.1);
}

.why-card:hover .why-icon-wrapper {
  transform: scale(1.15) translateY(-4px);
}

.why-icon {
  width: 24px;
  height: 24px;
  color: var(--gold);
}

.why-icon-wrapper.blue .why-icon {
  color: var(--blue);
}

.why-number {
  font-size: 2rem;
  font-weight: 800;
  color: var(--text-main);
  opacity: 0.1;
  transition: opacity 0.3s;
}

.why-card:hover .why-number {
  opacity: 0.3;
}

.why-title {
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--text-main);
  margin-bottom: 12px;
  letter-spacing: -0.01em;
}

.why-desc {
  font-size: 0.95rem;
  color: var(--text-muted);
  line-height: 1.6;
}

@media (max-width: 1024px) {
  .why-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .why-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }
  .why-card {
    padding: 24px;
    opacity: 1;
    transform: none;
    animation: none !important;
  }
}
</style>
