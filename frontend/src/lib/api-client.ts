/**
 * FIGTR Frontend API Client
 *
 * This module provides a centralized HTTP client for communicating with the
 * FIGTR backend API. It handles:
 * - Base URL configuration via environment variables
 * - Automatic token injection (authentication)
 * - Tenant context propagation
 * - Request/response interceptors
 * - Error handling and toast notifications
 *
 * Usage:
 *   import { apiClient } from "@/lib/api-client";
 *   const response = await apiClient.get("/students");
 */

import { toast } from "@/components/ui/use-toast";

// Environment variable for the API base URL.
// In Next.js, client-side env vars must be prefixed with NEXT_PUBLIC_.
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "/api";

// Request timeout in milliseconds.
const DEFAULT_TIMEOUT = 30000;

interface RequestOptions extends RequestInit {
  skipAuth?: boolean;
  skipErrorToast?: boolean;
}

class ApiError extends Error {
  public status: number;
  public data: unknown;

  constructor(status: number, message: string, data?: unknown) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.data = data;
  }
}

async function request<T>(
  endpoint: string,
  options: RequestOptions = {}
): Promise<T> {
  const { skipAuth = false, skipErrorToast = false, ...fetchOptions } = options;

  const url = endpoint.startsWith("http")
    ? endpoint
    : `${API_BASE_URL}${endpoint.startsWith("/") ? endpoint : `/${endpoint}`}`;

  const headers = new Headers(fetchOptions.headers);
  headers.set("Content-Type", "application/json");

  // Inject authentication token if available and not skipped.
  if (!skipAuth) {
    const token = typeof window !== "undefined" ? localStorage.getItem("auth_token") : null;
    if (token) {
      headers.set("Authorization", `Bearer ${token}`);
    }
  }

  // Abort controller for timeout.
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), DEFAULT_TIMEOUT);
  const signal = controller.signal;

  const response = await fetch(url, {
    ...fetchOptions,
    headers,
    signal,
    credentials: "include",
  });

  clearTimeout(timeout);

  const contentType = response.headers.get("content-type");
  let data: unknown;
  if (contentType && contentType.includes("application/json")) {
    data = await response.json();
  } else {
    data = await response.text();
  }

  if (!response.ok) {
    const error = new ApiError(
      response.status,
      (data as { message?: string })?.message || `HTTP ${response.status}`,
      data
    );

    if (!skipErrorToast && typeof window !== "undefined") {
      toast({
        title: "Request failed",
        description: error.message,
        variant: "destructive",
      });
    }

    throw error;
  }

  return data as T;
}

export const apiClient = {
  get: <T>(endpoint: string, options?: RequestOptions) =>
    request<T>(endpoint, { method: "GET", ...options }),
  post: <T>(endpoint: string, body?: unknown, options?: RequestOptions) =>
    request<T>(endpoint, {
      method: "POST",
      body: body ? JSON.stringify(body) : undefined,
      ...options,
    }),
  put: <T>(endpoint: string, body?: unknown, options?: RequestOptions) =>
    request<T>(endpoint, {
      method: "PUT",
      body: body ? JSON.stringify(body) : undefined,
      ...options,
    }),
  patch: <T>(endpoint: string, body?: unknown, options?: RequestOptions) =>
    request<T>(endpoint, {
      method: "PATCH",
      body: body ? JSON.stringify(body) : undefined,
      ...options,
    }),
  delete: <T>(endpoint: string, options?: RequestOptions) =>
    request<T>(endpoint, { method: "DELETE", ...options }),
};